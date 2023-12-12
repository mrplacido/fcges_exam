from rest_framework import response, serializers, status, views


class Exam1Serializer(serializers.Serializer):
    array = serializers.ListField()


class Exam1View(views.APIView):
    serializer_class = Exam1Serializer

    def post(self, request, *args, **kwargs):
        # ENDPOINT: http://localhost:8000/find_missing_int/
        # SAMPLE PAYLOAD:
        # {
        #     "array": [1, 3, 6, 4, 1, 2]
        # }

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            array = serializer.validated_data.get('array', [])
            result = self.missing_int(array)
            return response.Response({'result': result}, status=status.HTTP_200_OK)

        return response.Response({'error': 'Invalid data in the request'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def missing_int(A):
        # Remove non-positive integers and duplicates
        A = list(set(filter(lambda x: x > 0, A)))

        # If the array is empty, return 1
        if not A:
            return 1

        # Sort the array
        A.sort()

        # Find the smallest positive integer not present in the array
        missing = 1
        for num in A:
            if num == missing:
                missing += 1
            else:
                return missing

        return missing


class Exam2View(views.APIView):
    def post(self, request, *args, **kwargs):
        # Get parameters from request data
        a = int(request.data.get('a', 0))
        b = int(request.data.get('b', 0))
        k = int(request.data.get('k', 1))

        # Your find_divisible logic here
        count = self.find_divisible(a, b, k)
        return response.Response({'count': count}, status=status.HTTP_200_OK)

    def find_divisible(self, a, b, k):
        count = 0
        for num in range(a, b + 1):
            if num % k == 0:
                count += 1
        return count


class Exam3View(views.APIView):
    def post(self, request, *args, **kwargs):
        # Get array and rotation count from request data
        array = request.data.get('array', [])
        k = int(request.data.get('k', 0))

        # Your rotate logic here
        rotated_array = self.rotate(array, k)
        return response.Response({'rotated_array': rotated_array}, status=status.HTTP_200_OK)

    def rotate(self, A, k):
        n = len(A)

        # If the array is empty or k is 0, return the original array
        if n == 0 or k % n == 0:
            return A

        # Calculate the effective rotation by taking the remainder
        k = k % n

        # Perform the rotation using slicing
        rotated_array = A[-k:] + A[:-k]

        return rotated_array