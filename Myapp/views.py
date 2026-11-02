from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.http import JsonResponse


class JobView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "job_title": "Python Django Developer",
                "company": "ABC Technologies",
                "location": "Kochi",
                "job_type": "Full-time",
                "salary": "15000-25000",
                "description": "Looking for a Python Django developer.",
                "qualification": "BCA",
                "experience": 0,
                "skills": ["Python", "Django", "MySQL"],
                "is_active": True
            },
            {
                "id": 2,
                "job_title": "Frontend Developer",
                "company": "XYZ Solutions",
                "location": "Calicut",
                "job_type": "Internship",
                "salary": "8000-12000",
                "description": "Looking for a frontend developer.",
                "qualification": "Any Degree",
                "experience": 0,
                "skills": ["HTML", "CSS", "JavaScript"],
                "is_active": True
            }
        ]
        return JsonResponse(data, safe=False)


class CompanyView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "company_name": "ABC Technologies",
                "location": "Kochi",
                "email": "abc@gmail.com",
                "website": "https://abc.com",
                "industry": "Software Development",
                "description": "Software development company"
            },
            {
                "id": 2,
                "company_name": "XYZ Solutions",
                "location": "Calicut",
                "email": "xyz@gmail.com",
                "website": "https://xyz.com",
                "industry": "IT Services",
                "description": "IT service provider"
            }
        ]
        return JsonResponse(data, safe=False)


class CategoryView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "category_name": "Python Developer",
                "description": "Python development jobs"
            },
            {
                "id": 2,
                "category_name": "Frontend Developer",
                "description": "Frontend development jobs"
            },
            {
                "id": 3,
                "category_name": "Backend Developer",
                "description": "Backend development jobs"
            },
            {
                "id": 4,
                "category_name": "Data Analyst",
                "description": "Data analysis jobs"
            }
        ]
        return JsonResponse(data, safe=False)


class ApplicantView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "name": "Arun",
                "email": "arun@gmail.com",
                "phone": 9876543210,
                "qualification": "BCA",
                "skills": ["Python", "Django", "MySQL"],
                "experience": 0,
                "location": "Kochi"
            },
            {
                "id": 2,
                "name": "Rahul",
                "email": "rahul@gmail.com",
                "phone": 9876543211,
                "qualification": "MCA",
                "skills": ["Java", "Spring Boot"],
                "experience": 1,
                "location": "Calicut"
            }
        ]
        return JsonResponse(data, safe=False)


class ApplicationView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "applicant_id": 1,
                "job_id": 1,
                "application_date": "2026-11-01",
                "status": "Pending",
                "resume": "arun_resume.pdf"
            },
            {
                "id": 2,
                "applicant_id": 2,
                "job_id": 2,
                "application_date": "2026-11-02",
                "status": "Shortlisted",
                "resume": "rahul_resume.pdf"
            }
        ]
        return JsonResponse(data, safe=False)
