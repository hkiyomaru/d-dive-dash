# -*- coding: undecided -*-
class CreateLessons < ActiveRecord::Migration
  def change
    create_table :lessons do |t|
      t.integer :year
      t.string :classcode
      t.string :url
      t.string :title
      t.string :teacher
      t.string :season
      t.string :place
      t.string :time, default: "未"
      t.string :room, default: "未"

      t.timestamps
    end
  end
end
