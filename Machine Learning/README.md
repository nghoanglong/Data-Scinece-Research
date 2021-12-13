# Machine Learning roadmap and resource
Mọi kiến thức được mình học theo trình tự bên dưới, từ những khái niệm căn bản đến những phần nâng cao cần thiết. Tùy kiến thức mỗi người hiện đang có mà có thể bắt đầu từ những chỗ khác nhau, ko nhất thiết phải đọc hết từ đầu.
## Nhiệm vụ của Machine Learning
**Reading:**
+ Sách Machine Learning cơ bản - Chương 5, 5.1

+ [Machine Learning là gì?](https://khanh-personal.gitbook.io/ml-book-vn/machine-learning-la-gi)

**Notes:** Hiểu được nhiệm vụ và vai trò của các thuật toán machine learning 

## Các vấn đề với dữ liệu trong Machine Learning 
**Reading:**

Phần này vì tài liệu rất nhiều nên  bạn có thể tự research để có góc nhìn tổng quát. Một số tài liệu mình dùng như
+ Sách Machine Learning cơ bản - Chương 5, 5.2
+ Sách Hands-on ML - Part 1, Chap 1, Main challenges of ML, chỉ đọc 4 phần (insufficient, nonrepresentative, poor-quality, irrelevant)

**Notes:**

+ Biết được các vấn đề với dữ liệu trong machine learning 
+ Biết lí do tại sao lại chia ra thành các tập dữ liệu train, dev or validation, test
+ Tác dụng của tập validation hay còn gọi là dev? (cần biết về overfit trước) 
+ Trong trường hợp bộ dữ liệu nhỏ, cần biết thêm kiến thức về cross-validation (cần biết về overfit và validation)

## Các bài toán trong Machine Learning
**Reading:**
+ Sách Machine Learning cơ bản - Chương 5, 5.3

**Notes:** Biết được những nhóm bài toán trong machine learning 

## Các thuật toán trong Machine Learning
**Reading:**
+ Sách Machine Learning cơ bản - Chương 5, 5.4

**Notes:** Biết được các thuật toán trong machine learning
## Các khái niệm cơ bản
**Reading:**

Phần này vì tài liệu rất nhiều nên  bạn có thể tự research để có góc nhìn tổng quát. Một số tài liệu mình dùng như
+ [Khanh persional blog](https://khanh-personal.gitbook.io/ml-book-vn/khai-niem-co-ban)
+ Sách Machine Learning cơ bản

**Notes:**
+ Biết được  Observation và feature vector là gì?
+ Label là gì?
+ Model cơ bản là gì?
+ Loss function và objective function là gì?
+ Parameter
  + Biết sơ sơ parameter là những tham số khi train mà model có thể tự học được, ví dụ như weigts  **W** = [O1, O2, O3,...], biết rõ hơn ở những mục tiếp theo 
+ Hyper-parameter
  + Biết sơ sơ hyper-parameter là những tham số đã được gán cứng sẵn, nó ko được học qua quá trình train, ví dụ như learning rate,...
+ Hiểu được mô hình chung của các bài toán machine learning là đi tối ưu những hàm loss function bằng cách  đi tìm các tham số (parameter) tối ưu nhất

## Linear Regression
**Reading:**

+ [Machine Learning cơ bản](https://machinelearningcoban.com/2016/12/28/linearregression/)
+ Linear Regression - Normal Equation - Single Variable Implementation -> Folder Linear Regression
+ Linear Regression - Normal Equation - Multiple Variable Implementation -> Folder Linear Regression

**Notes:**
+ Hiểu được các khái niệm cơ bản ở trên như model, loss function, parameter, hyper-parameter 
+ Xác định linear regression ở đây là đang implementation dựa trên các phép biến đổi phức tạp, sau khi được học kiến thức về gradient descent ta sẽ có cách giải mới mà không cần biến đổi tính toán mà hoàn toàn  dựa vào đạo hàm
+ Biết được loss function của các bài toán LR (MSE, RMSE)

## Gradient Descent
**Reading:**

+ [Machine Learning cơ bản - part 1](https://machinelearningcoban.com/2017/01/12/gradientdescent/)
+ [Machine Learning cơ bản - part 2](https://machinelearningcoban.com/2017/01/16/gradientdescent2/)
+ Gradient Descent Implementation -> Folder Gradient Descent
+ Linear Regression - Gradient Descent - Single Variable Implementation -> Folder Linear Regression

**Notes:**
+ Biết cách ứng dụng gradient descent cho linear regression
+ Hiểu được gradient descent

## Logistic Regression
**Reading:**

+ [Machine learning cơ bản](https://machinelearningcoban.com/2017/01/27/logisticregression/)
+ [Machine learning in 2 Months](https://github.com/bangoc123/learn-machine-learning-in-two-months/tree/master/models/logistic-regression)
+ Logistic Regression - Binary Classification Implementation -> Folder Logistic Regression

**Notes:**
+ Hiểu được logistic regression, khái niệm cơ bản trong machine learning 

## Overfit và Underfit trong ML
**Reading:**

Phần này vì tài liệu rất nhiều nên  bạn có thể tự research để có góc nhìn tổng quát. Một số tài liệu mình dùng như
+ [Khanh personal-blog](https://khanh-personal.gitbook.io/ml-book-vn/chapter1/overfitting)
+ [Machine Learning Adrew Nguyen](https://youtu.be/xjRbUX0i_e0?list=PLDpRz2wA0qZzTcDLeXP5PSCfmQ96l9-Qr) -> Xem video [26, 27, 28, 29]

**Notes:**
+ Biết được thế nào là overfit và underfit
+ Regulization dùng để làm gì?
+ Cơ chế khắc phục overfit và underfit
 + lựa chọn feature to keep, lựa chọn 1 model khác, sử dụng regulization 
 + cách chia tập dataset, sử dụng cross-validation, nhìn learning curve và early stop, xem lại dữ liệu 

## Mối quan hệ giữa bias và variance
**Reading:**

+ [Bias và variance](https://forum.machinelearningcoban.com/t/moi-quan-he-danh-doi-giua-bias-va-variance/4173)
+ [Machine learning Andrew Nguyen](https://youtu.be/9XMeUBO4DY4?list=PLDpRz2wA0qZzTcDLeXP5PSCfmQ96l9-Qr) -> Xem video [48, 49]

**Notes:**
+ Biết được các trường hợp sau:
 + High bias: High error in training set dẫn tới việc high error in dev and test set → mô hình ko quan tấm lắm về dữ liệu train, nên bị underfitting, model quá đơn giản
 + High variance: low error in training set but high error in dev and test set → mô hình cố mô tả lại chính xác dữ liệu train, cho nên ko có tính khái quát, dẫn đến overfitting
 + Low bias và high variance: overfit
 + High bias và low variance: underfit
+ Biết được các trường hợp sau với regulization: 
 + Nếu regulization với hệ số lambda thấp, model sẽ bị overfit vì ko giảm được các weights
 + Nếu regulization với hệ số lambda cao, model sẽ bị underfit vì limit quá mức các weights

## Metrics for measurement
**Reading:**

+ [Machine learning Andrew Nguyen](https://youtu.be/83y817CiBI4?list=PLDpRz2wA0qZzTcDLeXP5PSCfmQ96l9-Qr) -> Xem video [54, 55]
+ [Machine learning cơ bản](https://machinelearningcoban.com/2017/08/31/evaluation/)
+ [Precision, recall, F1-score là gì?](https://math2it.com/hieu-confusion-matrix/)
+ [Ý nghĩa của R-squared, Adj R-squared](https://www.phamlocblog.com/2019/10/y-nghia-r-binh-phuong-hieu-chinh.html)
+ [Ý nghĩa của R-squared, Adj R-squared - Part 2](https://phantichspss.com/r-binh-phuong-r-binh-phuong-hieu-chinh-cong-thuc-y-nghia-cach-tinh-thu-cong-va-cach-tinh-bang-spss.html)
+ [Tính toán R-squared with Python from scratch, phần 1](https://www.codinground.com/calculating-r-squared-python/)
+ [Tính toán R-squared with Python from scratch, phần 2](https://pythonprogramming.net/how-to-program-r-squared-machine-learning-tutorial/)

**Notes:**
+ Biết được các phép đánh giá mô hình phân loại (bài toán multi-classification)
+ Biết được các phép đánh giá mô hình LR (R-squared, Adj R-squared)

## K-nearest Neighbors

**Reading:**
+ [Machine learning cơ bản](https://machinelearningcoban.com/2017/01/08/knn/)
+ K-nearest Neighbors Implementation -> Folder K-nearest Neighbors

**Notes:**
+ Hiểu lý thuyết K-nearest và cách implementation

## K-means Clustering
**Reading:**
+ [Machine Learning cơ bản](https://machinelearningcoban.com/2017/01/04/kmeans2/)
+ K-means Clustering Implementation -> Folder K-means Clustering

**Notes:**
+ Hiểu lý thuyết K-means và cách implementation

# References
+ [Sách Machine learning cơ bản](https://machinelearningcoban.com/)
+ [Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems 2nd](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291)
+ [Khanh personal-blog](https://khanh-personal.gitbook.io/ml-book-vn/)
