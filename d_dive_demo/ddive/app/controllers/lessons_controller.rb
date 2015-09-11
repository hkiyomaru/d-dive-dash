# -*- coding: utf-8 -*-
class LessonsController < ApplicationController

  def index
    @search = Lesson.search(params[:q])
    @lessons = @search.result
  end

  def show
    @lesson = Lesson.find(params[:id])
  end
  
  def edit
    @lesson = Lesson.find(params[:id])
  end

  def update
    @lesson = Lesson.find(params[:id])
    if @lesson.update(lesson_params)
      redirect_to lesson_path(@lesson.id)
    else
      render 'edit'
    end
  end

  # GET /lessons
  # GET /lessons.json
  def welcome
    @search = Lesson.search(params[:q])
  end

  def find
    @search = Lesson.search(params[:q])
    @lessons = @search.result
  end

  private
    def lesson_params
      params[:lesson].permit(:title, :teacher, :season,:time, :room)
    end

end
