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
      t.string :time
      t.string :room

      t.timestamps
    end
  end
end
